8A] Write a program to demonstrate static variable.

CODE:
#include<iostream.h>
#include<conio.h>
class item
{
private:
static int count;
int number;
public:
void getdata(int a)
{
number=a;
count++;
}
void getcount()
{
cout<<"Count= "<<count<<endl;
}
};
int item::count;
void main()
{
clrscr();
item a,b,c;
a.getcount();
b.getcount();
c.getcount();
a.getdata(100);
b.getdata(200);
c.getdata(300);



a.getcount();
b.getcount();
c.getcount();
getch();
}

8B:
8B] Write a program to demonstrate static function.

CODE:
#include<iostream.h>
#include<conio.h>
class test
{
private:
int code;
static int count;
public:
void setcode()
{
code=++count;
}
void showcode()
{
cout<<"Number= "<<code<<endl;
}
static void showcount()
{
cout<<"Count= "<<count<<endl;
}
};
int test::count;
void main()
{
clrscr();
test t1,t2;
t1.setcode();
t2.setcode();
test::showcount();
test t3;
t3.setcode();
test::showcount();
t1.showcode();
t2.showcode();
t3.showcode();
getch();
}

9A] Write a program to demonstrate the use of pointers.

CODE:
#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int a;
int *p;
p=&a;
a=5;
cout<<"The Value of a is= "<<*p<<endl;
cout<<”Address of a is= “<<p<<endl;
getch();
}

9B] Write a program to create a display() in a class, and access using pointer.

CODE:
#include<iostream.h>
#include<conio.h>
class ABC
{
public:
void display()
{
cout<<"In Class ABC."<<endl;
}
};
void main()
{
clrscr();
ABC a;
ABC *p;
p=&a;
p->display();
getch();
}

9C] Write a program to demonstrate the use of a virtual function.

CODE:
#include<iostream.h>
#include<conio.h>
class Base
{
public:
void display()
{
cout<<"Display Base "<<endl;
}
virtual void show()
{
cout<<"Show Base "<<endl;
}
};
class Derived:public Base
{
public:
void display()
{
cout<<"Display Derived "<<endl;
}
void show()
{
cout<<"Show Derived "<<endl;
}
};
void main()
{
clrscr();
Base B;
Derived D;
Base *bptr;
cout<<"bptr Points to Base "<<endl;
bptr=&B;
bptr->display();
bptr->show();
cout<<"bptr Points to Derived "<<endl;
bptr=&D;
bptr->display();
bptr->show();
getch();
}
//Practical 10.
10A] Write a program to demonstrate overloading of unary operator. 
CODE: 
#include<iostream.h> 
#include<conio.h> 
class space 
{ 
int x,y,z; 
public: 
void getdata(int a,int b,int c); 
void display(); 
void operator -(); 
}; 
void space::getdata(int a,int b,int c) 
{ 
x=a; 
y=b; 
z=c; 
} 
void space::display() 
{ 
cout<<"X= "<<x<<endl; 
cout<<"Y= "<<y<<endl; 
cout<<"Z= "<<z<<endl; 
} 
void space::operator -() 
{ 
x=-x; 
y=-y; 
z=-z; 
} 
void main() 
{ 
clrscr(); 
space s; 
s.getdata(10,-20,30); 
s.display(); -s; 
s.display(); 
getch(); 
}

10B] Write a program to demonstrate overloading of binary operator. 
CODE: 
#include<iostream.h> 
#include<conio.h> 
class complex 
{ 
float x,y; 
public: 
complex() 
{ 
} 
complex(float a,float b) 
{ 
x=a; 
y=b; 
} 
void display() 
{ 
cout<<x<<"+"<<y<<"i"<<endl; 
} 
complex operator +(complex c); 
}; 
complex complex::operator +(complex c) 
{ 
complex temp; 
temp.x=x+c.x; 
temp.y=y+c.y; 
return temp; 
} 
void main() 
{ 
clrscr(); 
complex c1(4.0,5.0); 
complex c2(8.0,4.0); 
complex c3; 
c1.display(); 
c2.display(); 
c3=c1+c2; 
c3.display(); 
getch(); 
}
Practical 7
C) Demonstrate ambiguity in Multiple Inheritance and resolve it. 
CODE: 
#include<iostream.h> 
#include<conio.h> 
class M 
{ 
public: 
void display() 
{ 
cout<<"In class M"<<endl; 
} 
}; 
class N 
{ 
public: 
void display() 
{ 
cout<<"In class N"<<endl; 
} 
}; 
class P:public M,public N 
{ 
public: 
void display() 
{ 
cout<<"In class P"<<endl; 
} 
}; 
void main() 
{ 
clrscr(); 
P P1; 
P1.M::display(); 
P1.N::display(); 
P1.display(); 
getch(); 
} 

D) Demonstrate ambiguity in Hybrid Inheritance and resolve it. 
CODE: 
#include<iostream.h> 
#include<conio.h> 
class A 
{ 
public: 
void show() 
{ 
cout<<"In class A"<<endl; 
} 
}; 
class B:public virtual A 
{ 
public: 
void show() 
{ 
cout<<"In class B"<<endl; 
} 
}; 
class C:public virtual A 
{ 
public: 
void show() 
{ 
cout<<"In class C"<<endl; 
} 
}; 
class D:public B,public C 
{ 
public: 
void show() 
{ 
cout<<"In class D"<<endl; 
} 
}; 
void main() 
{ 
clrscr(); 
D D1; 
D1.A::show(); 
D1.B::show(); 
D1.C::show(); 
D1.show(); 
getch(); 
}

E) Demonstrate Hierarchical Inheritance. 
CODE: 
#include<iostream.h> 
#include<conio.h> 
class shape 
{ 
public: 
void display() 
{ 
cout<<"Shape"<<endl; 
} 
}; 
class circle:public shape 
{ 
public: 
void area() 
{ 
cout<<"Circle"<<endl; 
} 
}; 
class square:public shape 
{ 
public: 
void area() 
{ 
cout<<"Square"<<endl; 
} 
}; 
void main() 
{ 
clrscr(); 
circle circle; 
square square; 
circle.display(); 
circle.area(); 
square.display(); 
square.area(); 
getch(); 
}
