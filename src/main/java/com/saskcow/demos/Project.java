package com.saskcow.demos;

import lombok.Data;

@Data
class Project {
	
	private String name;
	private String description;
    private String author;
	
	private String language;
	private String srcFolder;
	private String mainFile;
}
