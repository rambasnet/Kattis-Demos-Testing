/*
 * The MIT License
 *
 * Copyright 2019 Warren MacEvoy <wmacevoy@coloradomesa.edu>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

import java.util.Arrays;
import org.junit.Test;
import static org.junit.Assert.*;

// group test data into cases...
class Case {
    String name;
    int[] temperatures;
    int negatives;
    
    @Override
    public String toString() {
        return "testcase " + name + ": " + Arrays.toString(temperatures) + " -> " + negatives;
    }
    
            
    Case(String name) {

        this.name = name;
        switch (name) {
            case "example 1":
                temperatures = new int[]{5, -10, 15};
                negatives = 1;
                break;
            case "example 2":
                temperatures = new int[]{-14, -5, -39, -5, -7};
                negatives = 5;
                break;
            case "test 1":
                temperatures = new int[]{0, -10, 15};
                negatives = 1;
                break;
            case "test 2":
                temperatures = new int[]{0, 0, 0};
                negatives = 0;
                break;
            default:
                throw new IndexOutOfBoundsException();
        }
    }
    static String[] ALL = new String[]{"example 1", "example 2","test 1", "test 2"};

}

public class AppTest {

    // makes cases from their names, with default of all
    Case[] cases(String... names) {
        if (names.length == 0) {
            names = Case.ALL;
        }
        Case[] ans = new Case[names.length];
        for (int i = 0; i < ans.length; ++i) {
            ans[i] = new Case(names[i]);
        }
        return ans;
    }

    void testSolve(Case... cases) {
        for (Case test : cases) {
            System.out.println("solve " + test);
            App app = new App();
            app.temperatures = test.temperatures;
            app.solve();
            assertEquals(test.negatives, app.negatives);
        }
    }

    @Test
    public void testSolveAll() {
        testSolve(cases());
    }

    @Test
    public void testSolveExample1() {
        testSolve(cases("example 1"));
    }

    @Test
    public void testSolveExample2() {
        testSolve(cases("example 2"));
    }
}
