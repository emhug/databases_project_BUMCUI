# Create the Strain table
create table Strain(
	strain_id int not null auto_increment,
	species varchar(40),
	strain varchar(25),
	other_name varchar(25),
	plasmid varchar(15),
	wt_mutant varchar(25),
	mutations varchar(25),
	received_from varchar(100),
	reference_1 text,
	reference_2 text,
	tower varchar(5),
	microbiome1 enum('Biofuels', 'Marine', 'Soil', 'Human Gut', 'Freshwater') default null,
	microbiome2 enum('Biofuels', 'Marine', 'Soil', 'Human Gut', 'Freshwater') default null,
	mta_from varchar(15),
	kegg_genome varchar(10),
	media_komodo varchar(50),
	media_dsmz int,
	tempc_dsmz int,
	media_obs varchar(50),
	media_obs2 varchar(50),
	media_obs3 varchar(50),
	bacdive text,
	primary key(strain_id)) engine=InnoDB;

# Create the Lab table	
create table Lab(
	lab_id int not null auto_increment,
	PI varchar(30),
	address varchar(100),
	email varchar(50),
	phone varchar(20),
	primary key(lab_id)) engine=InnoDB;

# Create the Strain_Lab table, which shows which strains are studied at which labs
create table Strain_Lab(
	strain_id int not null,
	lab_id int not null,
	primary key(strain_id, lab_id),
	foreign key(strain_id) references Strain(strain_id),
	foreign key(lab_id) references Lab(lab_id)) engine=InnoDB;

# Create the Media table
create table Media(
	media_id int not null auto_increment,
	media enum('sBMS', 'MP'),
	primary key(media_id)) engine=InnoDB;

# Create the Sources table
create table Source(
	source_id int not null auto_increment,
	C_source varchar(30),
	primary key(source_id)) engine=InnoDB;

# Create the Experiment table
create table Experiment(
	strain_id int not null,
	media_id int not null,
	source_id int not null,
	run_date date,
	OD24hr float,
	OD48hr float,
	OD72hr float,
	notes text,
	primary key(strain_id, media_id, source_id, run_date),
	foreign key(strain_id) references Strain(strain_id),
	foreign key(media_id) references Media(media_id),
	foreign key(source_id) references Source(source_id)) engine=InnoDB;
