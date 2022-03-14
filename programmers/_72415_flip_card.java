import java.util.*;

public class _72415_flip_card {

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static class Point {

    }

    static class CardNode {

        int y, x;
        boolean isFlip;
        int f_y, f_x;

        @Override
        public String toString() {
            return "CardNode{" +
                "y=" + y +
                ", x=" + x +
                ", isFlip=" + isFlip +
                ", f_y=" + f_y +
                ", f_x=" + f_x +
                ", board='" + board + '\'' +
                '}';
        }

        String board;

        public CardNode(int y, int x, boolean isFlip, int f_y, int f_x, String board) {
            this.y = y;
            this.x = x;
            this.isFlip = isFlip;
            this.f_y = f_y;
            this.f_x = f_x;
            this.board = board;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            CardNode cardNode = (CardNode) o;

            if (y != cardNode.y) {
                return false;
            }
            if (x != cardNode.x) {
                return false;
            }
            if (isFlip != cardNode.isFlip) {
                return false;
            }
            if (f_y != cardNode.f_y) {
                return false;
            }
            if (f_x != cardNode.f_x) {
                return false;
            }
            return board.equals(((CardNode) o).board);
        }

        @Override
        public int hashCode() {
            int result = y;
            result = 31 * result + x;
            result = 31 * result + (isFlip ? 1 : 0);
            result = 31 * result + f_y;
            result = 31 * result + f_x;
            result = 31 * result + (board != null ? board.hashCode() : 0);
            return result;
        }
    }

    static class CardNodeWithCount {

        CardNode cardNode;
        int cnt;

        public CardNodeWithCount(CardNode cardNode, int cnt) {
            this.cardNode = cardNode;
            this.cnt = cnt;
        }
    }

    static int convertIndex(int y, int x) {
        return 4 * y + x;
    }

    static String switchToZeroFromChar(String board, char num) {
        StringBuilder temp = new StringBuilder(board);
        return temp.toString().replace(num, '0');
    }

    static String serialize(int[][] board) {
        StringBuilder builder = new StringBuilder();
        for (int[] row : board) {
            for (int num : row) {
                builder.append(num);
            }
        }

        return builder.toString();
    }

    static void printBoard(int[][] board) {
        for (int[] row : board) {
            StringBuilder builder = new StringBuilder();
            for (int num : row) {
                builder.append(num);
            }
            System.out.println(builder.toString());
        }
    }

    static boolean isEnd(String board) {
        for (int i = 0; i < board.length(); i++) {
            if (board.charAt(i) != '0') {
                return false;
            }
        }
        return true;
//        return board.indexOf('0') != -1;
    }

    static boolean isOOB(int y, int x) {
        return y >= 4 || y < 0 || x >= 4 || x < 0;
    }

    static boolean isOnEdgeByDirection(int y, int x, int d) {
        switch (d) {
            case 0:
                if (y == 0) {
                    return true;
                }
                break;
            case 1:
                if (y == 3) {
                    return true;
                }
                break;
            case 2:
                if (x == 0) {
                    return true;
                }
                break;
            case 3:
                if (x == 3) {
                    return true;
                }
                break;
            default:
                return false;
        }
        return false;
    }


    //    static boolean[][][] visit;
    static Set<CardNode> visit;


    public static int solution(int[][] board, int r, int c) {
        int answer = 40;

//        visit = new boolean[4][4][2];

        visit = new HashSet<>();

        ArrayDeque<CardNodeWithCount> q = new ArrayDeque<>();

        CardNode e = new CardNode(r, c, false, -1, -1, serialize(board));
        CardNodeWithCount e1 = new CardNodeWithCount(e, 0);
        q.addLast(e1);

        visit.add(e);

        while (!q.isEmpty()) {
            CardNodeWithCount cardNodeWithCount = q.pollFirst();
            CardNode poll = cardNodeWithCount.cardNode;
//            System.out.println(poll.board);


            for (int k = 0; k < 4; k++) {
                int ny = poll.y + dy[k];
                int nx = poll.x + dx[k];

                if (isOOB(ny, nx)) {
                    continue;
                }

                // ctrl 이동 , 0이 아닌곳을 만나면 멈춰야함
                while (poll.board.charAt(convertIndex(ny, nx)) == '0' && !isOnEdgeByDirection(ny,
                    nx, k)) {
                    ny = ny + dy[k];
                    nx = nx + dx[k];
                }

                CardNode newCardPair = new CardNode(ny, nx, poll.isFlip, poll.f_y,
                    poll.f_x, poll.board);

                if (visit.contains(newCardPair)) {
                    continue;
                }

                visit.add(newCardPair);
//                q.add();
                q.addLast(new CardNodeWithCount(newCardPair, cardNodeWithCount.cnt + 1));
            }

            for (int k = 0; k < 4; k++) {
                int ny = poll.y + dy[k];
                int nx = poll.x + dx[k];

                if (isOOB(ny, nx)) {
                    continue;
                }

                CardNode newCardPair = new CardNode(ny, nx, poll.isFlip, poll.f_y,
                    poll.f_x, poll.board);

                if (visit.contains(newCardPair)) {
                    continue;
                }

                visit.add(newCardPair);
                q.addLast(new CardNodeWithCount(newCardPair, cardNodeWithCount.cnt + 1));
            }

            if (poll.isFlip) {
                if (poll.board.charAt(convertIndex(poll.f_y, poll.f_x)) == poll.board.charAt(
                    convertIndex(poll.y, poll.x)) && !(poll.f_y==poll.y&&poll.f_x==poll.x)) {

                    String newBoard = switchToZeroFromChar(poll.board,
                        poll.board.charAt(convertIndex(poll.f_y, poll.f_x)));

                    if (isEnd(newBoard)) {
                        return cardNodeWithCount.cnt + 1;
                    }

                    CardNode newCardPair = new CardNode(poll.y, poll.x, false, -1, -1,
                        newBoard);

                    visit.add(newCardPair);
                    q.addLast(new CardNodeWithCount(newCardPair, cardNodeWithCount.cnt + 1));

                } else {
                    CardNode newCardPair = new CardNode(poll.y, poll.x, false, -1, -1,
                        poll.board);

                    if (visit.contains(newCardPair)) {
                        continue;
                    }

                    visit.add(newCardPair);
                    q.addLast(new CardNodeWithCount(newCardPair, cardNodeWithCount.cnt + 1));

                }

            } else {
                CardNode newCardPair = new CardNode(poll.y, poll.x, true, poll.y,
                    poll.x, poll.board);

                if (visit.contains(newCardPair)) {
                    continue;
                }

                visit.add(newCardPair);
                q.addLast(new CardNodeWithCount(newCardPair, cardNodeWithCount.cnt + 1));


            }
        }

        return answer;


    }

    public static void main(String[] args) {
        int[][] board = {{0, 0, 1, 0}, {1, 0, 0, 0}, {4, 4, 3, 2}, {0, 3, 2, 0}};
        System.out.println(solution(board, 2, 0));
    }

}
