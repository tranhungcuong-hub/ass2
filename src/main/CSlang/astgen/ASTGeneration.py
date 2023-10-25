import functools
from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *
from functools import reduce

class ASTGeneration(CSlangVisitor):

    def visitProgram(self, ctx: CSlangParser.ProgramContext):
        decl = []
        if ctx.class_decl():
            decl.extend([self.visit(x) for x in ctx.class_decl()])
        if ctx.class_prog():
            decl.extend([self.visit(ctx.class_prog())])
        
        return Program(decl)

    # /**** class ****/
    def visitClass_prog(self, ctx: CSlangParser.Class_progContext):
        classname = ctx.getChild(1).getText() if ctx.ID() else ctx.getChild(1).getText()
        memlist = self.visit(ctx.program_member_list())
        parentname = self.visitID(ctx.ID()) if ctx.ID() else None
        return ClassDecl(classname, memlist, parentname)

    def visitProgram_member_list(self, ctx: CSlangParser.Program_member_listContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            decl = []
            [decl.extend(self.visit(ctx.getChild(i))) for i in range(ctx.getChildCount())]
            return decl

    def visitProgramMainDecl(self, ctx: CSlangParser.ProgramMainDeclContext):
        id = ctx.getChild(1).getText()
        param = []
        return_typ = self.visit(ctx.return_type())
        block_stm = self.visit(ctx.main_block_stm())
        return [MethodDecl(id,param,return_typ,block_stm)]

    def visitClass_decl(self, ctx: CSlangParser.Class_declContext):
        classname = self.visitID(ctx.ID(1)) if ctx.INHERITANCE() else self.visitID(ctx.ID(0))
        memlist = []
        [memlist.extend(self.visit(x)) for x in ctx.members()]
        parentname = self.visitID(ctx.ID(0)) if ctx.INHERITANCE() else None
        return ClassDecl(classname, memlist, parentname)
    
    def visitMembers(self, ctx: CSlangParser.MembersContext):
        if ctx.programMainDecl():
            return self.visit(ctx.programMainDecl())
        return self.visit(ctx.attribute_decl()) if ctx.attribute_decl() else self.visit(ctx.method_decl())

    # /**** attribute_decl ****/
    def visitAttribute_decl(self, ctx: CSlangParser.Attribute_declContext):
        # no init
        if ctx.id_list():
            id_list = self.visit(ctx.id_list())
            attr_type = self.visit(ctx.attr_type())
            return [AttributeDecl(VarDecl(x, attr_type)) for x in id_list]
        # init
        else:
            mutability = self.visit(ctx.mutability())
            id = self.visitID(ctx.ID()) if ctx.ID() else self.visitID(ctx.AT_ID())
            val_decl = self.visit(ctx.val_decl())
            val_list_decl = [(id, val_decl)] + self.visit(ctx.val_list_decl())
            attr_type = val_list_decl[-1][1]
            id_list = [x[0] for x in val_list_decl[:-1]]
            val_decl_list = [x[1] for x in val_list_decl[:-1]]
            if mutability == 'const':
                return [AttributeDecl(ConstDecl(x, attr_type, y)) for x,y in zip(id_list,val_decl_list[::-1])]
            else:
                return [AttributeDecl(VarDecl(x, attr_type, y)) for x,y in zip(id_list,val_decl_list[::-1])]

    def visitVal_list_decl(self, ctx: CSlangParser.Val_list_declContext):
        if ctx.ASSIGN():
            return [('type', self.visit(ctx.attr_type()))]
        else:
            id = self.visitID(ctx.ID()) if ctx.ID() else self.visitID(ctx.AT_ID())
            val_decl = self.visit(ctx.val_decl())
            return [(id, val_decl)] + self.visit(ctx.val_list_decl())

    def visitMutability(self, ctx: CSlangParser.MutabilityContext):
        return 'const' if ctx.CONST() else 'var'

    def visitId_list(self, ctx: CSlangParser.Id_listContext):
        id = [self.visitID(ctx.ID())] if ctx.ID() else [self.visitID(ctx.AT_ID())]
        return id + self.visit(ctx.id_plist())

    def visitId_plist(self, ctx: CSlangParser.Id_plistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            id = [self.visitID(ctx.ID())] if ctx.ID() else [self.visitID(ctx.AT_ID())]
            return id + self.visit(ctx.id_plist())

    # def visitVal_list(self, ctx: CSlangParser.Val_listContext):
    #     return None

    # def visitVal_plist(self, ctx: CSlangParser.Val_plistContext):
    #     return None

    def visitVal_decl(self, ctx: CSlangParser.Val_declContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            return self.visitINTLIT(ctx.INTLIT())
        elif ctx.FLOATLIT():
            return self.visitFLOATLIT(ctx.FLOATLIT())
        elif ctx.STRINGLIT():
            return self.visitSTRINGLIT(ctx.STRINGLIT())
        elif ctx.BOOLLIT():
            return self.visitBOOLLIT(ctx.BOOLLIT())

    # /**** method_decl ****/
    def visitMethod_decl(self, ctx: CSlangParser.Method_declContext):
        method_decl = self.visit(ctx.nor_method()) if ctx.nor_method() else self.visit(ctx.con_method())
        block_stm = self.visit(ctx.block_stm())
        return [MethodDecl(method_decl[0], method_decl[1], method_decl[2], block_stm)]

    def visitNor_method(self, ctx: CSlangParser.Nor_methodContext):
        id = self.visitID(ctx.ID()) if ctx.ID() else self.visitID(ctx.AT_ID())
        param_list = self.visit(ctx.param_list())
        return_typ = self.visit(ctx.return_type())
        return (id, param_list, return_typ)

    def visitCon_method(self, ctx: CSlangParser.Con_methodContext):
        id = Id(ctx.CONSTRUCTOR().getText())
        param_list = self.visit(ctx.param_list())
        return_typ = VoidType()
        return (id, param_list, return_typ)

    def visitParam_list(self, ctx: CSlangParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            param = [self.visit(ctx.param())] + self.visit(ctx.param_plist())
            return reduce(lambda x, y: x + [VarDecl(i, y[-1]) for i in y[:-1]], param, [])

    def visitParam_plist(self, ctx: CSlangParser.Param_plistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.param_plist())

    def visitParam(self, ctx: CSlangParser.ParamContext):
        params = [self.visitID(ctx.ID())] + self.visit(ctx.params())
        params.extend([self.visit(ctx.type_name())])
        return params

    def visitParams(self, ctx: CSlangParser.ParamsContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            params = [self.visitID(ctx.ID())]
            return params + self.visit(ctx.params())

    def visitReturn_type(self, ctx: CSlangParser.Return_typeContext):
        if ctx.type_name():
            return self.visit(ctx.type_name())
        elif ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.array_type())

    def visitBlock_stm(self, ctx: CSlangParser.Block_stmContext):
        stm_list = []
        if ctx.getChildCount() != 0:
            stm_list = [self.visit(ctx.statement(i)) for i in range(ctx.getChildCount() -2)]
        return Block(stm_list)

    def visitMain_block_stm(self, ctx: CSlangParser.Main_block_stmContext):
        main_stm_list = []
        if ctx.getChildCount() != 0:
            main_stm_list = [self.visit(ctx.main_stm(i)) for i in range(ctx.getChildCount() -2)]
        return Block(main_stm_list)

    def visitType_name(self, ctx: CSlangParser.Type_nameContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return self.visitID(ctx.ID())

    def visitArray_type(self, ctx: CSlangParser.Array_typeContext):
        return ArrayType(ctx.INTLIT(), ctx.type_name())

    def visitAttr_type(self, ctx: CSlangParser.Attr_typeContext):
        return self.visit(ctx.type_name()) if ctx.type_name() else self.visit(ctx.array_type())

    # /**** Expressions ****/
    def visitExp(self, ctx: CSlangParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        return BinaryOp(ctx.CONCATENATION().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))

    def visitExp1(self, ctx: CSlangParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        if ctx.LT():
            return BinaryOp(ctx.LT().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.LE():
            return BinaryOp(ctx.LE().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.GE():
            return BinaryOp(ctx.GE().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))

    def visitExp2(self, ctx: CSlangParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        elif ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    def visitExp3(self, ctx: CSlangParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        elif ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))

    def visitExp4(self, ctx: CSlangParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        elif ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.INT_DIV():
            return BinaryOp(ctx.INT_DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))

    def visitExp5(self, ctx: CSlangParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))

    def visitExp6(self, ctx: CSlangParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        else:
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp6()))

    def visitExp7(self, ctx: CSlangParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        else:
            return ArrayCell(self.visit(ctx.exp7()), self.visit(ctx.index_operator()))

    def visitExp8(self, ctx: CSlangParser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        else:
            return FieldAccess(self.visit(ctx.exp8()), self.visit(ctx.exp9()))

    def visitExp9(self, ctx: CSlangParser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp10(0))
        else:
            return FieldAccess(self.visit(ctx.exp10(0)), self.visit(ctx.exp10(1)))

    def visitExp10(self, ctx: CSlangParser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        else:
            return NewExpr(self.visit(ctx.exp10()), self.visit(ctx.exp_list()))

    def visitOperands(self, ctx: CSlangParser.OperandsContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.ID():
            return self.visitID(ctx.ID())
        elif ctx.AT_ID():
            return self.visitID(ctx.AT_ID())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.INTLIT():
            return self.visitINTLIT(ctx.INTLIT())
        elif ctx.FLOATLIT():
            return self.visitFLOATLIT(ctx.FLOATLIT())
        elif ctx.BOOLLIT():
            return self.visitBOOLLIT(ctx.BOOLLIT())
        elif ctx.STRINGLIT():
            return self.visitSTRINGLIT(ctx.STRINGLIT())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())

    def visitExp_list(self, ctx: CSlangParser.Exp_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            res = []
            res = res + [self.visit(ctx.exp())] + self.visit(ctx.exp_list())
            return res
    
    def visitIndex_operator(self, ctx:CSlangParser.Index_operatorContext):
        expr = [self.visit(ctx.exp())]
        if ctx.getChildCount() == 3:
            return expr
        else: 
            exprs = self.visit(ctx.index_operator())
            return expr + exprs

    # /**** Member Access ****/
    def visitInstance_access(self, ctx: CSlangParser.Instance_accessContext):
        obj = self.visit(ctx.exp(0))
        method = self.visit(ctx.ID())
        return FieldAccess(obj, method)

    def visitStatic_attr_access(self, ctx: CSlangParser.Static_attr_accessContext):
        if ctx.ID():
            return FieldAccess(ctx.ID(), self.visit(ctx.AT_ID()))
        else:
            return FieldAccess(None, self.visit(ctx.AT_ID()))

    def visitMethod_access(self, ctx: CSlangParser.Method_accessContext):
        obj = self.visit(ctx.exp())
        method = self.visitID(ctx.ID())
        explist =  self.visit(ctx.exp_list())
        return CallStmt(obj, method, explist)

    def visitStatic_method_access(self, ctx: CSlangParser.Static_method_accessContext):
        obj = self.visit(ctx.ID()) if ctx.ID() else None
        method = self.visit(ctx.AT_ID())
        explist =  self.visit(ctx.exp_list())
        return CallStmt(obj, method, explist)

    # /**** Statements ****/
    def visitStatement(self, ctx: CSlangParser.StatementContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.arrayAssignmentStatement():
            return self.visit(ctx.arrayAssignmentStatement())
        elif ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.invocationStatement():
            return self.visit(ctx.invocationStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.block_stm():
            return self.visit(ctx.block_stm())

    def visitMain_stm(self, ctx: CSlangParser.Main_stmContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.arrayAssignmentStatement():
            return self.visit(ctx.arrayAssignmentStatement())
        elif ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.main_invocation_stm():
            return self.visit(ctx.main_invocation_stm())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.block_stm():
            return self.visit(ctx.block_stm())

    def visitVariableDeclaration(self, ctx: CSlangParser.VariableDeclarationContext):
        return ctx.visit(ctx.attribute_decl())

    def visitArrayDeclaration(self, ctx: CSlangParser.ArrayDeclarationContext):
        return None

    def visitAssignmentStatement(self, ctx: CSlangParser.AssignmentStatementContext):
        return Assign(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))

    # def visitScalarVariable(self, ctx: CSlangParser.ScalarVariableContext):
    #     return ctx.exp()

    # def visitIndexExpression(self, ctx: CSlangParser.IndexExpressionContext):
    #     return ArrayCell()

    def visitArrayAssignmentStatement(self, ctx: CSlangParser.ArrayAssignmentStatementContext):
        return None

    def visitReturnStatement(self, ctx: CSlangParser.ReturnStatementContext):
        return Return(ctx.exp())

    def visitContinueStatement(self, ctx: CSlangParser.ContinueStatementContext):
        return Continue()

    def visitBreakStatement(self, ctx: CSlangParser.BreakStatementContext):
        return Break()

    def visitIfStatement(self, ctx: CSlangParser.IfStatementContext):
        elseStm = self.visit(ctx.elseStatement()) if ctx.elseStatement() else None
        preStm = self.visit(ctx.statement) if ctx.statement else None
        return If(ctx.exp(), ctx.visit(ctx.block_stm()), preStm, elseStm)

    def visitElseStatement(self, ctx: CSlangParser.ElseStatementContext):
        return self.visit(ctx.block_stm())

    def visitForStatement(self, ctx: CSlangParser.ForStatementContext):
        return For(self.visit(ctx.initStm()), self.visit(ctx.conStm()), self.visit(ctx.postStm()),
                   self.visit(ctx.block_stm()))

    def visitInitStm(self, ctx: CSlangParser.InitStmContext):
        return Assign(self.visitID(ctx.ID()), self.visit(ctx.exp()))

    def visitConStm(self, ctx: CSlangParser.ConStmContext):
        return BinaryOp(self.visit(ctx.getChild(1)), self.visitID(ctx.ID()), self, self.visitINTLIT(ctx.INTLIT()))

    def visitPostStm(self, ctx: CSlangParser.PostStmContext):
        return Assign(self.visitID(ctx.ID()), self.visit(ctx.exp()))

    def visitInvocationStatement(self, ctx: CSlangParser.InvocationStatementContext):
        if ctx.method_access():
            return self.visit(ctx.method_access())
        if ctx.static_method_access():
            return self.visit(ctx.static_method_access())

    def visitMain_invocation_stm(self, ctx: CSlangParser.Main_invocation_stmContext):
        if ctx.method_access():
            return self.visit(ctx.method_access())
        if ctx.static_method_access():
            return self.visit(ctx.static_method_access())
        if ctx.static_attr_access():
            return self.visit(ctx.static_attr_access())
        if ctx.instance_access():
            return self.visit(ctx.instance_access())
    
    def visitArray_lit(self, ctx: CSlangParser.Array_litContext):
        value = [self.visit(ctx.element())] + self.visit(ctx.arraylit_list())
        return ArrayLiteral(value)

    def visitElement(self, ctx: CSlangParser.ElementContext):
        if ctx.INTLIT():
            return self.visitINTLIT(ctx.INTLIT())
        elif ctx.FLOATLIT():
            return self.visitFLOATLIT(ctx.FLOATLIT())
        elif ctx.BOOLLIT():
            return self.visitBOOLLIT(ctx.BOOLLIT())
        elif ctx.STRINGLIT():
            return self.visitSTRINGLIT(ctx.STRINGLIT())
        else:
            return self.visit(ctx.array_lit())
    
    def visitArraylit_list(self, ctx: CSlangParser.Arraylit_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.element())] + self.visit(ctx.arraylit_list())
    # helpers:
    def visitID(self, id):
        return Id(id.getText())

    def visitOP(self, op):
        return op.getText()

    def visitINTLIT(self, intlit):
        return IntLiteral(int(intlit.getText()))

    def visitFLOATLIT(self, floatlit):
        return FloatLiteral(float(floatlit.getText()))
    
    def visitSTRINGLIT(self, strlit):
        return StringLiteral(strlit.getText())
    
    def visitBOOLLIT(self, boollit):
        return BooleanLiteral(boollit.getText() == 'true')
    
    
