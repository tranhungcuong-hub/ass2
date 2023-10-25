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
            var a,b:int;
        }"""
        expect = """Program([ClassDecl(Program,[AttributeDecl(VarDecl(Id(a),IntType)),AttributeDecl(VarDecl(Id(b),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
    
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
   