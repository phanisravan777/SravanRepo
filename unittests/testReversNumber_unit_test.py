import org.junit.Test;
import static org.junit.Assert.*;

public class TestGFG {

    @Test
    public void testReversNumber() {
        // Basic Test Cases
        assertEquals(4321, GFG.reversNumber(1234));
        assertEquals(1, GFG.reversNumber(1));
        assertEquals(0, GFG.reversNumber(0));

        // Edge Test Cases
        assertEquals(987654321, GFG.reversNumber(123456789));
        assertEquals(2147483641, GFG.reversNumber(1463847412));
        assertEquals(-2147483641, GFG.reversNumber(-1463847412));
    }

    @Test
    public void testPalindrome() {
        // Basic Test Cases
        assertTrue(GFG.isPalindrome(12321));
        assertTrue(GFG.isPalindrome(1));
        assertFalse(GFG.isPalindrome(123));

        // Edge Test Cases
        assertTrue(GFG.isPalindrome(2147447412));
        assertFalse(GFG.isPalindrome(2147483647));
        assertTrue(GFG.isPalindrome(-2147447412));
    }
}