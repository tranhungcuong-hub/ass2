import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """class main {}"""
        expect = """Program([ClassDecl(Id(main),[])])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = """Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(a),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_302(self):
        """More complex program"""
        input = """class main {
            var a,b:int;
        }"""
        expect = """Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(a),IntType)),AttributeDecl(VarDecl(Id(b),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_303(self):
        """More complex program"""
        input = """class Program {
            var a,b:int = 2,3;
        }"""
        expect = """Program([ClassDecl(Program,[AttributeDecl(VarDecl(Id(a),IntType,IntLit(2))),AttributeDecl(VarDecl(Id(b),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304(self):
        """More complex program"""
        input = """class Program {
            var a,b:int = 2,3;
            func @main():void {}

        }"""
        expect = """Program([ClassDecl(Program,[AttributeDecl(VarDecl(Id(a),IntType,IntLit(2))),AttributeDecl(VarDecl(Id(b),IntType,IntLit(3))),MethodDecl(@main,[],VoidType,Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))

    def test_305(self):
        """More complex program"""
        input = """class object<-main{ const x, y, z: int = 1, 2, 3;
        var a, b: float;}"""
        expect = """Program([ClassDecl(Id(main),Id(object),[AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(z),IntType,IntLit(3))),AttributeDecl(VarDecl(Id(a),FloatType)),AttributeDecl(VarDecl(Id(b),FloatType))])])"""
        self.assertTrue(TestAST.test(input,expect,305))

    def test_306(self):
        """More complex program"""
        input = """class main{ func a(): void {}}"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(a),[],VoidType,Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test_307(self):
        """More complex program"""
        input = """class main{
        func foo  (a: int, b: float):void {}

        func @main():void{
            io.printInt(4);
        }}"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[Param(Id(a),IntType),Param(Id(b),FloatType)],VoidType,Block([])),MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(printInt),[IntLit(4)])]))])])"""

        self.assertTrue(TestAST.test(input,expect,307))
    
    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #         var b:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(VarDecl(Id("a"),IntType())),
    #          AttributeDecl(VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   