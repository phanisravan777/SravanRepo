import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGFG {

    @Test
    public void testReversNumber() {
        // Basic Test Cases
        assertEquals(321, GFG.reversNumber(123));
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
        assertEquals("Palindrome = Yes", GFG.main(12321));
        assertEquals("Palindrome = No", GFG.main(123));

        // Edge Test Cases
        assertEquals("Palindrome = Yes", GFG.main(1));
        assertEquals("Palindrome = Yes", GFG.main(0));
        assertEquals("Palindrome = No", GFG.main(123456789));
    }
}