import javax.swing.JFrame;

import org.math.plot.*;

public class TestGradDescent {
	public static void main(String[] args ){
		InitialData id = new InitialData();
		id.plotData();
		GradientDescent gd = new GradientDescent(id);
		gd.execute();
		gd.printConvergence();

	}
}