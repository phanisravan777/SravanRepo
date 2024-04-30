import org.junit.Test;
import static org.junit.Assert.*;

public class TestGFG {

    @Test
    public void testFibonacci() {
        // Test with N = 10
        assertEquals("0 1 1 2 3 5 8 13 21 34 ", GFG.Fibonacci(10));

        // Test with N = 0
        assertEquals("", GFG.Fibonacci(0));

        // Test with N = 1
        assertEquals("0 ", GFG.Fibonacci(1));

        // Test with N = 2
        assertEquals("0 1 ", GFG.Fibonacci(2));

        // Test with negative N
        try {
            GFG.Fibonacci(-1);
            fail("Should have thrown an exception");
        } catch (IllegalArgumentException e) {
            // Expected
        }
    }
}