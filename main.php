<!DOCTYPE html>
<html>
    <body>

        <?php
        
        pre_r($_POST);
        if(isset($_POST['submit'])){
            $filename = "C:\Users\ozany\Documents\GitHub\php_way\depo.txt";
            $file = fopen( $filename, "w" );

            if( $file == false ) {
                echo ( "Error in opening new file" );
                exit();
            }

            fwrite( $file, $_POST['display_content']);
            fclose( $file );
        }
        
        ?>

        <?php
        /*
        pre_r($_POST);
        if(isset($_POST['submit'])){
            $txt = $_POST['display_content'];

        }
        */
        ?>

        <?php
        /*
        pre_r($_POST);
        if(isset($_POST['submit'])){
            echo "First name: " .$_POST['display_content'].'<br />';
        }
        */
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
