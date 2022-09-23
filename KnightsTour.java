class KnightsTour {
  
  static final int N = 8;

  static int knightTour(int sol[][], int i, int j, int steps, int x[], int y[]) {
    if (steps == N*N)
      return 1;

    for(int k=0; k<8; k++) {
      int a = i+x[k]; //next i
      int b = j+y[k]; //next j

      if(checkMove(a, b, sol)==1) {
        sol[a][b] = steps;
        if (knightTour(sol, a, b, steps+1, x, y)==1)
          return 1;
        sol[a][b] = -1; // if next step is not valid then move back
      }
    }
    return 0;
  }

  static int checkMove(int i, int j, int sol[][]) {
    if (i>=1 && i<=N && j>=1 && j<=N && sol[i][j]==-1) {
        return 1;
    }
    return 0;
  }

  static int KnightTour() {
    int[][] sol = new int[N+1][N+1];

    for(int i=1; i<=N; i++) {
      for(int j=1; j<=N; j++) {
        sol[i][j] = -1;
      }
    }

    int x[] = {2, 1, -1, -2, -2, -1, 1, 2};
    int y[] = {1, 2, 2, 1, -1, -2, -2, -1};

    sol[1][1] = 0; // starting the knight at(1, 1)

    if (knightTour(sol, 1, 1, 1, x, y)==1) {
      for(int i=1; i<=N; i++) {
        for(int j=1; j<=N; j++) {
          System.out.print("["+sol[i][j]+"] ");
        }
        System.out.println();
      }
      return 1;
    }
    return 0;
  }

  public static void main(String[] args) {
    KnightTour();
  }
}