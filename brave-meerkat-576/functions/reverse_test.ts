import { SlackFunctionTester } from "deno-slack-sdk/mod.ts";
import { assertEquals } from "https://deno.land/std@0.153.0/testing/asserts.ts";
import ReverseFunction from "./reverse.ts";

const { createContext } = SlackFunctionTester("reverse");

Deno.test("Reverse string function test", async () => {
  assertEquals("oof", "oof");
});
