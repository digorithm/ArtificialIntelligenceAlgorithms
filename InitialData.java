import javax.swing.JFrame;
 
// This program uses JMathPlot, a package for producing Matlab-style graphs
//   Get it at http://code.google.com/p/jmathplot/
//   or just delete the blocks of code that use it.
import org.math.plot.*;

public class InitialData{
	public static double[] x = {2, 4, 6, 8};
	public static double[] y = {2, 5, 5, 8};


	public void plotData(){
		Plot2DPanel plot = new Plot2DPanel();
		plot.addScatterPlot("X-Y", this.x, this.y);
		JFrame frame = new JFrame("Original X-Y Data");
		frame.setContentPane(plot);
		frame.setSize(600, 600);
		frame.setVisible(true);
	}
}