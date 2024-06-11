class Solution {
    long sumOfSeries(long n) {
        // code here
        long s = 0;
        while (n != 0) {
            s += n * n * n;
            n--;
        }
        return s;
    }
}