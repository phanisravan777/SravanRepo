import org.junit.Test;
import static org.junit.Assert.*;

public class TestGFG {

    @Test
    public void testReversNumber() {
        assertEquals(4321, GFG.reversNumber(1234));
        assertEquals(1, GFG.reversNumber(1));
        assertEquals(0, GFG.reversNumber(0));
        assertEquals(987654321, GFG.reversNumber(123456789));
        assertEquals(123456789, GFG.reversNumber(987654321));
    }

    @Test
    public void testPalindrome() {
        assertTrue(GFG.isPalindrome(12321));
        assertTrue(GFG.isPalindrome(1));
        assertFalse(GFG.isPalindrome(1234));
        assertTrue(GFG.isPalindrome(0));
        assertTrue(GFG.isPalindrome(1234567654321));
        assertFalse(GFG.isPalindrome(123456789));
    }
}