<div >
  <h2>All Customers</h2>
  <table class="table ">
    <thead>
      <tr>
        <th class="text-center">S.N.</th>
        <th class="text-center">Client ID </th>
        <th class="text-center">Username </th>
        <th class="text-center">password </th>
        <th class="text-center">first name </th>
        <th class="text-center">last name </th>
        <th class="text-center">middle name </th>
        <th class="text-center">Contact Number</th>
        <th class="text-center">Email</th>
        <th class="text-center">request</th>
      </tr>
    </thead>
    <?php
      include_once "../config/dbconnect.php";
      $sql="SELECT * from clients";
      $result=$conn-> query($sql);
      $count=1;
      if ($result-> num_rows > 0){
        while ($row=$result-> fetch_assoc()) {
           
    ?>
    <tr>
      <td><?=$count?></td>
      <td><?=$row["client_id"]?></td> 
      <td><?=$row["username"]?></td>
      <td><?=$row["password"]?></td>
      <td><?=$row["f_name"]?></td>
      <td><?=$row["l_name"]?></td>
      <td><?=$row["m_name"]?></td>
      <td><?=$row["p_number"]?></td>
      <td><?=$row["email"]?></td>
      <td><?=$row["request"]?></td>
    </tr>
    <?php
            $count=$count+1;
           
        }
    }
    ?>
  </table>