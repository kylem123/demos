package main.java.demos;

public class Project {
	
	private String name;
	private String description;
    private String author;
	
	private String language;
	private String srcFolder;
	private String mainFile;
	
	public Project(String s1, String s2, String s3, String s4, String s5, String s6) {
		name = s1;
		description = s2;
		author = s3;
		
		language = s4;
		srcFolder = s5;
		mainFile = s6;
	}
	
	public String getName() {
		return name;
	}
	
	public String getDescription() {
		return description;
	}
	
	public String getAuthor() {
		return author;
	}
	
	public String getLanguage() {
		return language;
	}
	
	public String getSrcFolder() {
		return srcFolder;
	}
	
	public String getMainFile() {
		return mainFile;
	}
}
