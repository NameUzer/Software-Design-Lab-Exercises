-- SQLite
CREATE TABLE ADVENTURE_TRIP (
    TRIP_ID int,
    TRIP_NAME varchar(75),
    START_LOCATION varchar(50),
    STATE varchar(2),
    DISTANCE int,
    MAX_GRP_SIZE int,
    TYPE varchar(20),
    SEASON varchar(20)
    );

select *from ADVENTURE_TRIP;

INSERT INTO ADVENTURE_TRIP VALUES ( 45,
            'Jay Peak',
            'Jay',
            'VT',
            8,
            8,
            'Hiking',
            'Summer'
            );
INSERT INTO ADVENTURE_TRIP VALUES ( 46,
            'Jovert',
            'joe',
            'LA',
            8,
            8,
            'Swimming',
            'Summer'
            );


select *from MUSIC_TRIP;




