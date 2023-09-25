<?php
class TokenAuth {
    public function generateToken($username, $password) {
        // Concatenate username and password with a separator
        $token = $username . '|' . $password;
        // Encrypt the token using the password as the secret key
        return hash('sha256', $token . $password);
    }

    public function validateToken($token, $username, $password) {
        // Generate a new token with the provided username and password
        $newToken = $this->generateToken($username, $password);
        // Compare the new token with the provided token
        return hash_equals($newToken, $token);
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $auth = new TokenAuth();
    $username = $_POST['username'];
    $password = $_POST['password'];
    $token = $auth->generateToken($username, $password);
    
    echo "Welcome, " . htmlspecialchars($username) . "! Your token is: " . htmlspecialchars($token);
}
?>
