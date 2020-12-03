CREATE TABLE IF NOT EXISTS cyclones (
                    cid varchar(50) NOT NULL,
                    name varchar(50) NOT NULL,
                    region varchar(50) NOT NULL,
                    url varchar(150),
                    img varchar(255),
                    speed varchar(45),
                    type  varchar(45),
                    updated_at TIMESTAMP NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (cid)
)