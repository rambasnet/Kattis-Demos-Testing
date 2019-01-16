/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cold;

import java.io.PrintStream;
import java.util.Scanner;

/**
 *
 * @author warren
 */
public class Solver {

    Scanner in;
    PrintStream out;

    public static void main(String... args) throws Exception {
        Solver solver = new Solver();
        solver.in = new Scanner(System.in);
        solver.out = System.out;
        solver.run();
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
