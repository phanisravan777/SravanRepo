import org.junit.Test;
import static org.junit.Assert.*;

public class TestGFG {

    @Test
    public void testReversNumber() {
        assertEquals(4321, GFG.reversNumber(1234));
        assertEquals(1, GFG.reversNumber(1));
        assertEquals(0, GFG.reversNumber(0));
        assertEquals(987654321, GFG.reversNumber(123456789));
    }

    @Test
    public void testPalindrome() {
        int n = 12321;
        int reverseN = GFG.reversNumber(n);
        assertEquals(n, reverseN);

        n = 123456;
        reverseN = GFG.reversNumber(n);
        assertNotEquals(n, reverseN);
    }
}