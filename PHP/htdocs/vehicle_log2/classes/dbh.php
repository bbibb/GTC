<?php
class Dbh
{
    protected $host = '127.0.0.1:3308';
    protected $user = 'bryanb';
    protected $pwd = 'aside-FLARE-grandam';
    private $dbName = 'cpt283bibb_vehicle_log';

    protected function dbConnect(): PDO
    {
        $dsn = 'mysql:host=' . $this->host . ';dbname=' . $this->dbName;
        $pdo = new PDO($dsn, $this->user, $this->pwd);
//        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        return $pdo;
    }
}