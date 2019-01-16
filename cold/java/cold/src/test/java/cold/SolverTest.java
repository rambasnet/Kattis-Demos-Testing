/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cold;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Scanner;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author warren
 */
public class SolverTest {
    String in1 = "3" + System.lineSeparator()
            + "5 -10 15" + System.lineSeparator();
    int[] dat1 = new int[]{5, -10, 15};
    int ans1 = 1;
    String out1 = "1" + System.lineSeparator();

    String in2 = "5" + System.lineSeparator()
            + "-14 -5 -39 -5 -7" + System.lineSeparator();
    int[] dat2 = new int[]{-14, -5, -39, -5, -7};
    int ans2 = 5;
    String out2 = "5" + System.lineSeparator();


    // advanced black-box test setting and recovering stdin/stdout
    // if this is the only test you did not write a testable solution
    // sample data 1
    @Test
    public void testMain1() throws Exception {
        PrintStream saveOut = System.out;
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        PrintStream baPS = new PrintStream(baOut);
        System.setOut(baPS);

        InputStream saveIn = System.in;
        ByteArrayInputStream baIn = new ByteArrayInputStream(in1.getBytes("UTF-8"));
        System.setIn(baIn);
        
        // restore the streams or you will break other tests...
        try {
            Solver.main(null);
        } finally {
            System.setOut(saveOut);
            System.setIn(saveIn);
        }
        assertEquals(out1, baOut.toString());
    }

    // advanced black-box test setting and recovering stdin/stdout
    // if this is the only test you did not write a testable solution
    // sample data 2
    @Test
    public void testMain2() throws Exception {
        PrintStream saveOut = System.out;
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        PrintStream baPS = new PrintStream(baOut);
        System.setOut(baPS);

        InputStream saveIn = System.in;
        ByteArrayInputStream baIn = new ByteArrayInputStream(in2.getBytes("UTF-8"));
        System.setIn(baIn);

        // restore the streams or you will break other tests...
        try {
            Solver.main(null);
        } finally {
            System.setOut(saveOut);
            System.setIn(saveIn);
        }
        assertEquals(out2, baOut.toString());
    }

    // full run sample 1 without mucking with stdin/stdout
    @Test
    public void testRun1() {
        System.out.println("run");
        Solver instance = new Solver();
        instance.in = new Scanner(in1);
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        instance.out = new PrintStream(baOut);
        instance.run();
        assertEquals(out1, baOut.toString());
    }

    // full run sample 2 without mucking with stdin/stdout
    @Test
    public void testRun2() {
        System.out.println("run");
        Solver instance = new Solver();
        instance.in = new Scanner(in2);
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        instance.out = new PrintStream(baOut);
        instance.run();
        assertEquals(out2, baOut.toString());
    }

    // test correct read sample 1
    @Test
    public void testRead1() {
        Solver instance = new Solver();
        instance.in = new Scanner(in1);
        instance.read();
        assertArrayEquals(dat1, instance.temperatures);
    }

    // test correct read sample 2
    @Test
    public void testRead2() {
        Solver instance = new Solver();
        instance.in = new Scanner(in2);
        instance.read();
        assertArrayEquals(dat2, instance.temperatures);
    }

    // test solve 1 only (not read/write)
    @Test
    public void testSolve1() {
        System.out.println("solve");
        Solver instance = new Solver();
        instance.temperatures = Arrays.copyOf(dat1,dat1.length);
        instance.solve();
        assertEquals(ans1, instance.negatives);
    }

    // test solve 2 only (not read/write)
    @Test
    public void testSolve2() {
        System.out.println("solve");
        Solver instance = new Solver();
        instance.temperatures = Arrays.copyOf(dat2,dat2.length);
        instance.solve();
        assertEquals(ans2, instance.negatives);
    }

    // test write format only (not read/solve)
    public void testWrite1() {
        System.out.println("write");
        Solver instance = new Solver();
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        instance.out = new PrintStream(baOut);
        instance.negatives = ans1;
        instance.write();
        assertEquals(out1, baOut.toString());
    }

    // test write format only (not read/solve)
    public void testWrite2() {
        System.out.println("write");
        Solver instance = new Solver();
        ByteArrayOutputStream baOut = new ByteArrayOutputStream();
        instance.out = new PrintStream(baOut);
        instance.negatives = ans2;
        instance.write();
        assertEquals(out2, baOut.toString());
    }

}
