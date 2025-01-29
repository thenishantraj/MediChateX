import React, { useState } from 'react';
import { TextInput, Button, View, Text } from 'react-native';
import axios from 'axios';

const Signup = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = async () => {
    try {
      const response = await axios.post('http://localhost:5000/signup', { email, password });
      console.log(response.data);
      navigation.navigate('Home');
    } catch (error) {
      console.error("Error signing up:", error);
    }
  };

  return (
    <View>
      <Text>Signup</Text>
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Signup" onPress={handleSignup} />
    </View>
  );
};

export default Signup;
