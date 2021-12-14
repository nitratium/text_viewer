<!DOCTYPE html>
<html>
    <body>

        <?php
        pre_r($_POST);
        if(isset($_POST['submit'])){
            $filename = "/var/www/depo.txt";
            $file = fopen( $filename, "w" );

            if( $file == false ) {
                echo ( "Error in opening new file" );
                exit();
            }

            fwrite( $file, $_POST['display_content']);
            fclose( $file );
        }
        ?>

        <form action="" method="POST">
            Content: <input type="text" name="display_content" value="">
            <input type="submit" name="submit" value="Submit">
        </form>

        <?php
        function pre_r($array){
            echo'<pre>';
            print_r($array);
            echo'</pre>';
        }
        ?>

    </body>
</html>
