import java.util.*;

public class _64064_banned_id {

    class Solution {

        int userN;
        int banN;

        boolean[] visited;
        String[] user_id;
        String[] banned_id;
        HashSet<String> result;

        public int solution(String[] user_id, String[] banned_id) {

            userN = user_id.length;
            banN = banned_id.length;
            this.user_id = user_id;
            this.banned_id = banned_id;
            this.result = new HashSet<>();
            this.visited = new boolean[8];

            if(userN==banN) return 1;

            dfs(0, "");

            return result.size();
        }

        private void dfs(int banIdIdx, String answer) {
            if (banIdIdx == banN) {
                String[] split = answer.split(",");
                Arrays.sort(split);
                StringBuilder s = new StringBuilder();
                for (String s1 : split) {
                    s.append(s1);
                }

//                System.out.println(s);
                this.result.add(s.toString());
                return;
            }
            for (int i = 0; i < userN; i++) {
                if (visited[i] || !isPossible(user_id[i], banned_id[banIdIdx])) {
                    continue;
                }
                visited[i] = true;
                dfs(banIdIdx + 1, answer + "," + user_id[i]);
                visited[i] = false;
            }

        }


        private boolean isPossible(String candidate, String ban) {
            if (candidate.length() != ban.length()) {
                return false;
            }

            for (int i = 0; i < candidate.length(); i++) {
                if (ban.charAt(i) == '*') {
                    continue;
                }

                if (candidate.charAt(i) != ban.charAt(i)) {
                    return false;
                }
            }
            return true;
        }
    }
}
