<?php
    

    
    if (isset($_POST['login'])){
        $con = new mysqli('localhost', 'root', '', 'test');
        $us = $_POST['username'];
        $ps = $_POST['password'];
        $query = "SELECT * FROM user WHERE username = '$us' AND password = '$ps'";
        $result = $con->query($query);


        if($result->num_rows >= 1){
            header('Location: index.php');
        }else{
            $con->close();
            header('Location: login.html');
            echo "<script> alert('Invalid username or password')</script>"; 
        }
    }
?>