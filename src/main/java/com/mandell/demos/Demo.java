package demo;

import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

public class Demo extends StateBasedGame {

	public static AppGameContainer app;

	public static int width = 720, height = 720;

	public Demo() {
		super("Demo Library (By Kyle Mandell)");
	}

	@Override
	public void initStatesList(GameContainer gc) throws SlickException {
		addState(new MainState());

		enterState(0);
	}
	
	public static void main(String[] args) throws SlickException {
		app = new AppGameContainer(new Demo());
		app.setDisplayMode(width, height, false);
		app.setTargetFrameRate(60);
		app.setShowFPS(false);
		app.start();
	}
}