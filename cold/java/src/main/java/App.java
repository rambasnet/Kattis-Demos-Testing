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



import java.io.PrintStream;
import java.util.Scanner;

/**
 *
 * @author Warren MacEvoy <wmacevoy@gmail.com>
 * 
 * Solves the "cold" problem in a testable manner testable using JUnit4
 * 
 *   https://open.kattis.com/problems/cold
 * 
 * 
 */

public class App {

    Scanner in;
    PrintStream out;

    public static void main(String [] args) throws Exception {
        App main = new App();
        main.in = new Scanner(System.in);
        main.out = System.out;
        main.run();
    }

    void run() {
        read();
        solve();
        write();
    }

    int[] temperatures;

    void read() {
        int n = in.nextInt();
        temperatures = new int[n];
        for (int i = 0; i < n; ++i) {
            temperatures[i] = in.nextInt();
        }
    }

    int negatives;

    void solve() {
        negatives = 0;
        for (int i = 0; i < temperatures.length; ++i) {
            if (temperatures[i] < 0) {
                ++negatives;
            }
        }
    }

    void write() {
        out.println(negatives);
    }

}
