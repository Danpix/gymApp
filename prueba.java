import javax.swing.JOptionPane;

public class prueba {

    public static void main(String[] args) {
        System.out.println("Hola");

        for (int i = 0; i < 10; i++) {
            System.out.println("DDF y PJ");
        }

        String input = JOptionPane.showInputDialog("no amigo");
        JOptionPane.showMessageDialog(null, input);
    }    
}
