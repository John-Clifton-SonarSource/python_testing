public class JavaTesting {

    public static int complicatedStuff() {
        int a = 1;
        int b = 2;
        int c = 3;
        int d = 4;
        int e = 5;
        int f = 6;
        int g = 7;
        int h = 8;
        int total = 0;

        if (a < b) {
            total++;
            if (b < c) {
                total++;
                if (c < d) {
                    total++;
                    if (e < f) {
                        total++;
                        if (f < g) {
                            total++;
                            if (g < h) {
                                total++;
                            }
                        }
                    }
                }
            }
        }
    
        return total;
    }


}