import java.lang.*;
public class checkNumeric {
public static boolean isNumeric(String str, int n)
{
    for (int i = 0; i &lt; n; i++) {

        if ((str.charAt(i) == '0') ||(str.charAt(i) == '1') || (str.charAt(i)== '2') ||(str.charAt(i) == '3') ||(str.charAt(i) == '4')||(str.charAt(i) == '5';) ||(str.charAt(i) == '6') ||(str.charAt(i) =='7') ||(str.charAt(i) == '8') ||(str.charAt(i) == '9'))
          {
            return true;
          }
        else 
          {
            return false;
          }
        }
    return false;
}
public static void main(String args[])
  {
    String str = &quot;1234&quot;;
    int len = str.length();
    if (isNumeric(str, len))
      {
        System.out.println(“String is Numeric” );
      }
    else
      {
        System.out.println( “String is not Numeric” );
      }
  }
}
