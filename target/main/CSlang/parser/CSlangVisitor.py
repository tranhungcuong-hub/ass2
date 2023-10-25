# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_prog.
    def visitClass_prog(self, ctx:CSlangParser.Class_progContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#program_member_list.
    def visitProgram_member_list(self, ctx:CSlangParser.Program_member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#programMainDecl.
    def visitProgramMainDecl(self, ctx:CSlangParser.ProgramMainDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_decl.
    def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#members.
    def visitMembers(self, ctx:CSlangParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl.
    def visitAttribute_decl(self, ctx:CSlangParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#val_list_decl.
    def visitVal_list_decl(self, ctx:CSlangParser.Val_list_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mutability.
    def visitMutability(self, ctx:CSlangParser.MutabilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_list.
    def visitId_list(self, ctx:CSlangParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_plist.
    def visitId_plist(self, ctx:CSlangParser.Id_plistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#val_list.
    def visitVal_list(self, ctx:CSlangParser.Val_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#val_plist.
    def visitVal_plist(self, ctx:CSlangParser.Val_plistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#val_decl.
    def visitVal_decl(self, ctx:CSlangParser.Val_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_decl.
    def visitMethod_decl(self, ctx:CSlangParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#nor_method.
    def visitNor_method(self, ctx:CSlangParser.Nor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#con_method.
    def visitCon_method(self, ctx:CSlangParser.Con_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_list.
    def visitParam_list(self, ctx:CSlangParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_plist.
    def visitParam_plist(self, ctx:CSlangParser.Param_plistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params.
    def visitParams(self, ctx:CSlangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_type.
    def visitReturn_type(self, ctx:CSlangParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stm.
    def visitBlock_stm(self, ctx:CSlangParser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#main_block_stm.
    def visitMain_block_stm(self, ctx:CSlangParser.Main_block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#type_name.
    def visitType_name(self, ctx:CSlangParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_type.
    def visitAttr_type(self, ctx:CSlangParser.Attr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp.
    def visitExp(self, ctx:CSlangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp1.
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp2.
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp3.
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp4.
    def visitExp4(self, ctx:CSlangParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp5.
    def visitExp5(self, ctx:CSlangParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp6.
    def visitExp6(self, ctx:CSlangParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp7.
    def visitExp7(self, ctx:CSlangParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp8.
    def visitExp8(self, ctx:CSlangParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp9.
    def visitExp9(self, ctx:CSlangParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp10.
    def visitExp10(self, ctx:CSlangParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operands.
    def visitOperands(self, ctx:CSlangParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_list.
    def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_plist.
    def visitExp_plist(self, ctx:CSlangParser.Exp_plistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_access.
    def visitInstance_access(self, ctx:CSlangParser.Instance_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_attr_access.
    def visitStatic_attr_access(self, ctx:CSlangParser.Static_attr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_access.
    def visitMethod_access(self, ctx:CSlangParser.Method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_access.
    def visitStatic_method_access(self, ctx:CSlangParser.Static_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#obj_creation.
    def visitObj_creation(self, ctx:CSlangParser.Obj_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statement.
    def visitStatement(self, ctx:CSlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#main_stm.
    def visitMain_stm(self, ctx:CSlangParser.Main_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CSlangParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:CSlangParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:CSlangParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#scalarVariable.
    def visitScalarVariable(self, ctx:CSlangParser.ScalarVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#indexExpression.
    def visitIndexExpression(self, ctx:CSlangParser.IndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrayAssignmentStatement.
    def visitArrayAssignmentStatement(self, ctx:CSlangParser.ArrayAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#returnStatement.
    def visitReturnStatement(self, ctx:CSlangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continueStatement.
    def visitContinueStatement(self, ctx:CSlangParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#breakStatement.
    def visitBreakStatement(self, ctx:CSlangParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ifStatement.
    def visitIfStatement(self, ctx:CSlangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#elseStatement.
    def visitElseStatement(self, ctx:CSlangParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#forStatement.
    def visitForStatement(self, ctx:CSlangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#initStm.
    def visitInitStm(self, ctx:CSlangParser.InitStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#conStm.
    def visitConStm(self, ctx:CSlangParser.ConStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#postStm.
    def visitPostStm(self, ctx:CSlangParser.PostStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#invocationStatement.
    def visitInvocationStatement(self, ctx:CSlangParser.InvocationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#main_invocation_stm.
    def visitMain_invocation_stm(self, ctx:CSlangParser.Main_invocation_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_lit.
    def visitArray_lit(self, ctx:CSlangParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#element.
    def visitElement(self, ctx:CSlangParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraylit_list.
    def visitArraylit_list(self, ctx:CSlangParser.Arraylit_listContext):
        return self.visitChildren(ctx)



del CSlangParser