from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from src.main.CSlang.utils.AST import *
from functools import reduce

class ASTGeneration(CSlangVisitor):

    def visitProgram(self, ctx: CSlangParser.ProgramContext):
        decl = []
        if ctx.class_decl():
            decl.extends([self.visit(x) for x in ctx.class_decl()])
        if ctx.class_prog():
            decl.extends([self.visit(ctx.class_prog())])

        return Program(decl)

    # /**** class ****/
    def visitClass_prog(self, ctx: CSlangParser.Class_progContext):
        return ClassDecl(ctx.ID().getText(), self.visitProgram_member_list())

    def visitProgram_member_list(self, ctx: CSlangParser.Program_member_listContext):
        if(ctx.getChildCount() == 0):
            return self.visitProgram_main_decl()
        elif(ctx.getChildCount() == 1):
            return self.visitAttribute_decl()
        else:
            return self.visitMethod_decl()

    def visitProgramMainDecl(self, ctx: CSlangParser.ProgramMainDeclContext):
        return ctx.programMainDecl(self.visitMain_block_stm())

    def visitClass_decl(self, ctx: CSlangParser.class_decl):
        return ClassDecl(ctx.ID().getText(), self.visitMembers())

    # /**** attribute_decl ****/
    def visitAttribute_decl(self, ctx: CSlangParser.Attribute_declContext):
        return AttributeDecl(self.visitVal_list_decl())

    def visitVal_list_decl(self, ctx: CSlangParser.Val_list_declContext):
        return None

    def visitMutability(self, ctx: CSlangParser.MutabilityContext):
        return None

    def visitId_list(self, ctx: CSlangParser.Id_listContext):
        return None

    def visitId_plist(self, ctx: CSlangParser.Id_plistContext):
        return None

    def visitVal_list(self, ctx: CSlangParser.Val_listContext):
        return None

    def visitVal_plist(self, ctx: CSlangParser.Val_plistContext):
        return None

    def visitVal_decl(self, ctx: CSlangParser.Val_declContext):
        return None

    # /**** method_decl ****/
    def visitMethod_decl(self, ctx: CSlangParser.Method_declContext):
        return None

    def visitNor_method(self, ctx: CSlangParser.Nor_methodContext):
        return None

    def visitCon_method(self, ctx: CSlangParser.Con_methodContext):
        return None

    def visitParam_list(self, ctx: CSlangParser.Param_listContext):
        return None

    def visitParam_plist(self, ctx: CSlangParser.Param_plistContext):
        return None

    def visitParam(self, ctx: CSlangParser.ParamContext):
        return None

    def visitParams(self, ctx: CSlangParser.ParamsContext):
        return None

    def visitReturn_type(self, ctx: CSlangParser.Return_typeContext):
        return None

    def visitBlock_stm(self, ctx: CSlangParser.Block_stmContext):
        return None

    def visitMain_block_stm(self, ctx: CSlangParser.Main_block_stmContext):
        return None

    def visitType_name(self, ctx: CSlangParser.Type_nameContext):
        return None

    def visitArray_type(self, ctx: CSlangParser.Array_typeContext):
        return None

    def visitAttr_type(self, ctx: CSlangParser.Attr_typeContext):
        return None

    # /**** Expressions ****/
    def visitExp(self, ctx: CSlangParser.ExpContext):
        return None

    def visitExp1(self, ctx: CSlangParser.Exp1Context):
        return None

    def visitExp2(self, ctx: CSlangParser.Exp2Context):
        return None

    def visitExp3(self, ctx: CSlangParser.Exp3Context):
        return None

    def visitExp4(self, ctx: CSlangParser.Exp4Context):
        return None

    def visitExp5(self, ctx: CSlangParser.Exp5Context):
        return None

    def visitExp6(self, ctx: CSlangParser.Exp6Context):
        return None

    def visitExp7(self, ctx: CSlangParser.Exp7Context):
        return None

    def visitExp8(self, ctx: CSlangParser.Exp8Context):
        return None

    def visitExp9(self, ctx: CSlangParser.Exp9Context):
        return None

    def visitExp10(self, ctx: CSlangParser.Exp10Context):
        return None

    def visitOperands(self, ctx: CSlangParser.OperandsContext):
        return None

    def visitExp_list(self, ctx: CSlangParser.Exp_listContext):
        return None

    def visitExp_plist(self, ctx: CSlangParser.Exp_plistContext):
        return None

    # /**** Member Access ****/
    def visitInstance_access(self, ctx: CSlangParser.Instance_accessContext):
        return None

    def visitStatic_attr_access(self, ctx: CSlangParser.Static_attr_accessContext):
        return None

    def visitMethod_access(self, ctx: CSlangParser.Method_accessContext):
        return None

    def visitStatic_method_access(self, ctx: CSlangParser.Static_method_accessContext):
        return None

    # /**** OBJECT CREATION ****/
    def visitObj_creation(self, ctx: CSlangParser.Obj_creationContext):
        return None

    # /**** Statements ****/
    def visitStatement(self, ctx: CSlangParser.StatementContext):
        return None

    def visitMain_stm(self, ctx: CSlangParser.Main_stmContext):
        return None

    def visitVariableDeclaration(self, ctx: CSlangParser.VariableDeclarationContext):
        return None

    def visitArrayDeclaration(self, ctx: CSlangParser.ArrayDeclarationContext):
        return None

    def visitAssignmentStatement(self, ctx: CSlangParser.AssignmentStatementContext):
        return None

    def visitScalarVariable(self, ctx: CSlangParser.ScalarVariableContext):
        return None

    def visitIndexExpression(self, ctx: CSlangParser.IndexExpressionContext):
        return None

    def visitArrayAssignmentStatement(self, ctx: CSlangParser.ArrayAssignmentStatementContext):
        return None

    def visitReturnStatement(self, ctx: CSlangParser.ReturnStatementContext):
        return None

    def visitContinueStatement(self, ctx: CSlangParser.ContinueStatementContext):
        return None

    def visitBreakStatement(self, ctx: CSlangParser.BreakStatementContext):
        return None

    def visitIfStatement(self, ctx: CSlangParser.IfStatementContext):
        return None

    def visitElseStatement(self, ctx: CSlangParser.ElseStatementContext):
        return None

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

    # helpers:
    def visitID(self, id):
        return Id(id.getText())

    def visitOP(self, op):
        return op.getText()

    def visitINTLIT(self, intlit):
        return IntLiteral(int(intlit.getText()))
