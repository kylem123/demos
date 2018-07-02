package main.java.demos;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.gui.MouseOverArea;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

public class MainState extends BasicGameState {

	private static String pythonLocation;
	
	private static final String text = "Collection of demo programs, solely for the use of Mr D McArthur.";
	private static final Color bgColour = new Color(240, 255, 255);
	private static final Color projectColour = new Color(230, 230, 250);
	private static final Color projectColour2 = new Color(176, 224, 230);
	
	private static ArrayList<Project> projects = new ArrayList<>();
	private static ArrayList<MouseOverArea> buttons = new ArrayList<>();
	
	@Override
	public int getID() {
		return 0;
	}
	
	@Override
	public void init(GameContainer gc, StateBasedGame sbg) throws SlickException {
		File python = new File("projects/python");
		BufferedReader brp = null;
		try {
			brp = new BufferedReader(new FileReader(python.getPath()));
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		try {
			pythonLocation = brp.readLine();
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		try {
			brp.close();
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		
		File dir = new File("projects");
		
		for(File file : dir.listFiles()) {
			if(!file.isDirectory()) {
				if(file.getName().contains(".project")) {
					BufferedReader br = null;
					try {
						br = new BufferedReader(new FileReader(file.getPath()));
					} catch (FileNotFoundException e) {
						e.printStackTrace();
					}
					try {
					    String line = br.readLine();
					    ArrayList<String> lines = new ArrayList<String>();
					    
					    while (line != null) {
					        lines.add(line);
					        line = br.readLine();
					    }
					    
					    br.close();
					    
					    Project project = new Project(lines.get(1), lines.get(4), lines.get(7), lines.get(10), lines.get(13), lines.get(16));
					    
					    projects.add(project);
					    
					    int lineNum = (projects.size() - 1) / 2;
					    int pos = (projects.size() - 1) % 2;
					    
					    int x = 20 + (pos * 340);
						int y = 20 + (lineNum * 140);
					    
					    MouseOverArea button = new MouseOverArea(gc, new Image("src/button.png"), x + 5, y + 65, 290, 30) {
					    	@Override
					    	public void mousePressed(int button, int mx, int my) {
					    		if(mx >= getX() && my >= getY() && mx <= (getX() + getWidth()) && my <= (getY() + getHeight())) {	
						    		try {
//										Process p = Runtime.getRuntime().exec("cmd /c start cmd.exe /k " + pythonLocation + " " + dir.getAbsolutePath() + "/" + project.getMainFile());
                                        Process p = Runtime.getRuntime().exec(String.format("cmd /c start cmd.exe /k %s %s/%s", pythonLocation, dir.getAbsolutePath(), project.getMainFile()));
									} catch (IOException e) {
										e.printStackTrace();
									}
					    		}
					    	}
					    };
					    
					    button.setNormalColor(new Color(173, 216, 230));
					    button.setMouseOverColor(new Color(135, 206, 250));
					    
					    buttons.add(button);
					} 
					catch (IOException e) {
						e.printStackTrace();
					}
				}
			}
		}
	}

	@Override
	public void render(GameContainer gc, StateBasedGame sbg, Graphics g) {
		g.setBackground(bgColour);
		
		g.setColor(Color.black);
		g.drawString(text, (Demo.width / 2) - (g.getFont().getWidth(text) / 2), Demo.height - g.getFont().getHeight(text));
		
		int line = -1;
		for(int i = 0; i < projects.size(); i++) {
			Project project = projects.get(i);
			
			if(i % 2 == 0) {
				line++;
			}
			
			int x = 20 + ((i % 2) * 340);
			int y = 20 + (line * 140);
			
			g.setColor(projectColour);
			g.fillRect(x, y, 300, 60);
			
			g.setColor(Color.black);
			g.drawString(project.getName(), x + 150 - (g.getFont().getWidth(project.getName()) / 2), y);
			
			g.setColor(Color.lightGray);
			g.drawString(project.getDescription(), x + 150 - (g.getFont().getWidth(project.getDescription()) / 2), y + 20);
			
			g.setColor(Color.gray);
			String author = "By " + project.getAuthor();
			g.drawString(author, x + 150 - (g.getFont().getWidth(author) / 2), y + 40);
			
			g.setColor(projectColour2);
			g.fillRect(x, y + 60, 300, 40);
			
			buttons.get(i).render(gc, g);
			
			g.setColor(Color.black);
			String start = "Start " + project.getName();
			g.drawString(start, x + 150 - (g.getFont().getWidth(start) / 2), y + 80 - (g.getFont().getHeight(start) / 2));
		}
	}

	@Override
	public void update(GameContainer gc, StateBasedGame sbg, int delta) {
		
	}

}
