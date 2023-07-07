<?php
    include_once "../config/dbconnect.php";
    
    if(isset($_POST['upload']))
    {
       
        $ProductName = $_POST['p_name'];
        $desc= $_POST['p_desc'];
        $price = $_POST['p_price'];
        $category = $_POST['category'];
        $service_id = $_POST['id'];
            
        // $name = $_FILES['file']['name'];
        // $temp = $_FILES['file']['tmp_name'];
    
        // $location="./uploads/";
        // $image=$location.$name;

        // $target_dir="../uploads/";
        // $finalImage=$target_dir.$name;

        // move_uploaded_file($temp,$finalImage);

         $insert = mysqli_query($conn,"INSERT INTO services
         (service_id, service_name, service_description,category,unit_price) 
         VALUES ($service_id,'$ProductName','$desc',$category,$price)");
 
         if(!$insert)
         {
             echo mysqli_error($conn);
         }
         else
         {
             echo "Records added successfully.";
         }
     
    }
    else {
        echo "<script>alert('fail')</script>";
    }
        
?>