<?php
include('classes/dbh.php');

class Test extends Dbh {

    private $db;

    function __construct() {
        $this->db = new Dbh();
        $this->db = $this->db->dbConnect();
    }
    public function getVehicles()
    {
        $statement = "SELECT * FROM vehicles ORDER BY vehicle_make ASC";
        $query = $this->db->prepare($statement);
        $query->execute();
        $vehicles = $query->fetchAll();
        return $vehicles;
        }
    }

?>
