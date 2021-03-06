import React from "react";
import styled from "styled-components/native";
import Who from "./Who";
import Where from "./Where";
import BusinessApplication from "./ProfileScreens/BusinessApplication";
import BusinessManagement from "./ProfileScreens/BusinessManagement";
import NotificationSetting from "./ProfileScreens/NotificationSetting";
import ProfileEdit from "./ProfileScreens/ProfileEdit";
import ServiceCenter from "./ProfileScreens/ServiceCenter";
import StoreApplication from "./ProfileScreens/StoreApplication";
import StoreHistory from "./ProfileScreens/StoreHistory";
import Subscription from "./ProfileScreens/Subscription";
import ViewMore from "./ProfileScreens/ViewMore";
import BadgeDescription from "./ProfileScreens/ViewMore/BadgeDescription";
import BusinessPartnership from "./ProfileScreens/ViewMore/BusinessPartnership";
import Roadpick from "./ProfileScreens/ViewMore/Roadpick";
import Terms from "./ProfileScreens/ViewMore/Terms";
import BadgeManagement from "./ProfileScreens/BusinessManagement/BadgeManagement";
import BenefitManagement from "./ProfileScreens/BusinessManagement/BenefitManagement";
import CustomerAnalysis from "./ProfileScreens/BusinessManagement/CustomerAnalysis";
import BusinessEdit from "./ProfileScreens/BusinessManagement/BusinessEdit";
import { MainNavigator } from "./TabScreens";
import { createStackNavigator } from "@react-navigation/stack";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import { MaterialIcons } from "@expo/vector-icons";

const Stack = createStackNavigator();

const Home = () => {
  const insets = useSafeAreaInsets();
  return (
    <Stack.Navigator
      screenOptions={{
        cardStyle: { backgroundColor: "#ffffff" },
        headerTitleStyle: {
          fontSize: 24,
          color: "black",
        },
        headerTitleAlign: "center",
        headerBackTitleVisible: false,
        headerBackImage: () => {
          return (
            <MaterialIcons
              name="keyboard-backspace"
              size={26}
              style={{ marginLeft: 10 }}
            />
          );
        },
      }}
    >
      <Stack.Screen
        name="MainNavigator"
        component={MainNavigator}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Who"
        component={Who}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Where"
        component={Where}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="BusinessApplication"
        component={BusinessApplication}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="BusinessManagement"
        component={BusinessManagement}
        options={{ headerTitle: "???????????? ??????" }}
      />
      <Stack.Screen
        name="NotificationSetting"
        component={NotificationSetting}
        options={{ headerTitle: "?????? ??????" }}
      />
      <Stack.Screen
        name="ProfileEdit"
        component={ProfileEdit}
        // options={{ headerTitle: "????????? ??????" }}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="BusinessEdit"
        component={BusinessEdit}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="ServiceCenter"
        component={ServiceCenter}
        options={{ headerTitle: "?????? ?????? ?????? (FAQ)" }}
      />
      <Stack.Screen
        name="StoreApplication"
        component={StoreApplication}
        options={{ headerTitle: "????????????" }}
      />
      <Stack.Screen
        name="StoreHistory"
        component={StoreHistory}
        options={{ headerTitle: "??? ?????? ????????????" }}
      />
      <Stack.Screen
        name="Subscription"
        component={Subscription}
        options={{ headerTitle: "????????????" }}
      />
      <Stack.Screen
        name="ViewMore"
        component={ViewMore}
        options={{ headerTitle: "?????????" }}
      />
      <Stack.Screen
        name="BadgeDescription"
        component={BadgeDescription}
        options={{ headerTitle: "?????? ??????" }}
      />
      <Stack.Screen
        name="BusinessPartnership"
        component={BusinessPartnership}
        options={{ headerTitle: "???????????? ??????" }}
      />
      <Stack.Screen
        name="Roadpick"
        component={Roadpick}
        options={{ headerTitle: "????????? ??????" }}
      />
      <Stack.Screen
        name="Terms"
        component={Terms}
        options={{ headerTitle: "????????????" }}
      />
      <Stack.Screen
        name="BadgeManagement"
        component={BadgeManagement}
        options={{ headerTitle: "?????? ??????" }}
      />
      <Stack.Screen
        name="BenefitManagement"
        component={BenefitManagement}
        options={{ headerTitle: "?????? ??????" }}
      />
      <Stack.Screen
        name="CustomerAnalysis"
        component={CustomerAnalysis}
        options={{ headerTitle: "????????? ??????" }}
      />
    </Stack.Navigator>
  );
};

export default Home;

const Container = styled.View`
  align-items: center;
  padding-top: ${({ insets: { top } }) => top}px;
  padding-bottom: ${({ insets: { bottom } }) => bottom}px;
  padding-right: ${({ insets: { right } }) => right}px;
  padding-left: ${({ insets: { left } }) => left}px;
`;

const StyledText = styled.Text`
  font-size: 30px;
  margin: 10px;
`;
