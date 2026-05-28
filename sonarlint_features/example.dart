class ParentClass {
  bool doSomething(){/*...*/}
}
class FirstChildClass extends ParentClass {
  bool doSomething(){/*...*/}  // Noncompliant
}