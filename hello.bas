class hello(){
    function adds(a as integer,b as integer)as integer{
        return a + b;
    }
    function subs(a as integer,b as integer)as integer{
        return a - b;
    }
    function muls(a as integer,b as integer)as integer{
        return a * b;
    }
    function divs(a as integer,b as integer)as integer{
        return a \ b;
    }
    sub main(){
        dim s as string="hello world....\n";
        print s;
    }
}