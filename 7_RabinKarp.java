import java.util.*;
import java.lang.*;

public class RabinKarp {
    
    private static int base = 13;
    private static int modulo = 31;
    
    public static void main(String[] args) {
        String text = "mississippippissi";
        String pattern = "ippi";
        System.out.println("Indexing begins with 0");
        printAllMatchingOccurrences(text, pattern);
        
        String pattern2 = "issip";
        int patternHash2 = computeHash(pattern2);
        System.out.println("Pattern is " + pattern2 + " Pattern Hash is " + patternHash2);
    }
    
    private static void printAllMatchingOccurrences(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int highestPower = power(base, m-1);
        int patternHash = computeHash(pattern);
        System.out.println("Pattern is " + pattern + " Pattern Hash is " + patternHash);
        
        int textHash = computeHash(text.substring(0,m));
        System.out.println(text.substring(0,m) + " : " + textHash);
        
        for(int i=0;i<n-m+1;i++) {
            // System.out.println(text.substring(i, i+m));
            if(textHash == patternHash && pattern.equals(text.substring(i, i+m))) {
                System.out.println("Pattern found starting at index : " + i);
            }
            
            if(i != n-m) {
                // System.out.println(text.substring(i, i+m+1));
                textHash = rollingHash(textHash, text.substring(i, i+m+1), highestPower);
                System.out.println(text.substring(i+1, i+m+1) + " : " + textHash);
            }
        }
    }
    
    private static int rollingHash(int textHash, String window, int highestPower) {
        // System.out.println("Window " + window);
        // int newTextHash = (((textHash - ((window.charAt(0) - 'a') * highestPower) % modulo) * base) % modulo + (window.charAt(window.length() - 1) - 'a')) % modulo;
        
        int firstChar = window.charAt(0) - 'a';
        int lastChar = window.charAt(window.length() - 1) - 'a';
        int newTextHash = (textHash % modulo - (firstChar * highestPower) % modulo) % modulo;
        newTextHash = (newTextHash % modulo * base % modulo) % modulo;
        newTextHash = (newTextHash % modulo + lastChar % modulo) % modulo;
        return (newTextHash + modulo) % modulo;
    }
    
    private static int computeHash(String pattern) {
        int i;
        int m = pattern.length();
        int hashValue = 0;
        
        int highestPower = power(base, m-1);
        // System.out.println("highestPower is " + highestPower);
        int weight = highestPower;
        
        for(i=0;i<m;i++) {
            int offset = pattern.charAt(i) - 'a';
            // System.out.println(pattern.charAt(i) + " : " + offset);
            hashValue = (hashValue + (offset * weight) % modulo) % modulo;
            weight = weight/base;
            // System.out.println("weight is " + weight);
        }
        return hashValue;
    }
    
    public static int power(int x, int y)
    {
        int temp;
        if (y == 0)
            return 1;
        temp = power(x, y / 2);
 
        if (y % 2 == 0)
            return temp * temp;
        else {
            if (y > 0)
                return x * temp * temp;
            else
                return (temp * temp) / x;
        }
    }
}
