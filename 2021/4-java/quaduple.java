import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.io.File;  
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.TreeMap;


public class quaduple {
    private ArrayList<ArrayList<ArrayList<String>>> boards 
    = new ArrayList<ArrayList<ArrayList<String>>>();

    public boolean in(ArrayList<Integer> list, int num) {
        for (Integer integer : list) {
            if (integer == num) return true;
        }
        return false;
    }

    public int calculateBoard(ArrayList<ArrayList<String>> board, String result) {
        int lastNum = Integer.parseInt(result);
        int score = 0;
        for (List<String> row : board){
            System.out.println(row.toString());
            for (String num : row) {
                int numInt = Integer.parseInt(num);
                score += numInt;
            }
        }
        score = lastNum * score;
        return score;
    }

    public void treatResults(String[] results){
        for (String result : results) 
            for (ArrayList<ArrayList<String>> board : boards) 
                for (ArrayList<String> row : board){
                    if (row.remove(result))System.out.println(row.toString());
                    if (row.size() == 0) {
                        System.out.println("Found");
                        System.out.println(calculateBoard(board, result));
                        return;
                    }
                }
    }


    public static void main(String[] args) {
        quaduple bingo = new quaduple();
        try {
            Scanner myReader = new Scanner(new File("input4.txt"));
            String[] results = myReader.nextLine().split(",");
            TreeMap<Integer, List<String>> boardTreeMap= new TreeMap<Integer, List<String>>();
            int counter = 0; 
            ArrayList<ArrayList<String>> board = new ArrayList<ArrayList<String>>();
            ArrayList<String> row = new ArrayList<String>();

            while (myReader.hasNextLine()) {
                for (int i = 0; i < 5; i++) {
                    String data = myReader.nextLine();
                    if ("".equals(data))data = myReader.nextLine();
                    String[] line = data.split(" ");
                    row.clear();
                    for (String string : line)if (!"".equals(string)) row.add(string);
                    board.add(row);
                    boardTreeMap.put(counter, row);
                    //System.out.println(board.toString());
                }
                counter++;
                bingo.boards.add(board);
                System.out.println(bingo.boards.toString());  
                board.clear();
            }
            bingo.boards.add(board);
            //System.out.println(bingo.boards.toString());
            bingo.treatResults(results);
            myReader.close();
        } 
        catch (FileNotFoundException e) { 
            System.out.println(e.getMessage());
        }
    }
}