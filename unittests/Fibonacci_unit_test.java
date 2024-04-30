import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestFibonacci {

    @Test
    public void testFibonacciBasic() {
        // Test with small positive number
        assertEquals(GFG.Fibonacci(5), "0 1 1 2 3");
        // Test with 1
        assertEquals(GFG.Fibonacci(1), "0");
    }

    @Test
    public void testFibonacciEdge() {
        // Test with 0
        assertEquals(GFG.Fibonacci(0), "");
        // Test with negative number
        assertThrows(IllegalArgumentException.class, () -> GFG.Fibonacci(-1));
    }
}