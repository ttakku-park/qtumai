import React from "react";
import styled from "styled-components/native";
import { WebView } from "react-native-webview";
import { URI } from "../../config";

const ProfileEdit = ({ navigation }) => {
  return (
    <Container>
      <WebView
        source={{ uri: `${URI}/profile/profileedit` }}
        onMessage={(event) =>
          event.nativeEvent.data === "Success!"
            ? navigation.navigate("Profile")
            : null
        }
      />
    </Container>
  );
};

export default ProfileEdit;

const Container = styled.View`
  flex: 1;
`;
