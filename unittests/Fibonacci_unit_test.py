import org.junit.Test;
import static org.junit.Assert.*;

public class TestFibonacci {

    @Test
    public void testBasic() {
        assertEquals(GFG.Fibonacci(0), "");
        assertEquals(GFG.Fibonacci(1), "0");
        assertEquals(GFG.Fibonacci(2), "0 1");
        assertEquals(GFG.Fibonacci(3), "0 1 1");
    }

    @Test
    public void testEdge() {
        assertEquals(GFG.Fibonacci(-1), "");
        assertEquals(GFG.Fibonacci(Integer.MAX_VALUE), "");
    }
}