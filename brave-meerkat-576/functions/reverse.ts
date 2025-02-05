import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";

/**
 * Functions are reusable building blocks of automation that accept
 * inputs, perform calculations, and provide outputs. Functions can
 * be used independently or as steps in workflows.
 * https://api.slack.com/automation/functions/custom
 */
export const ReverseFunctionDefinition = DefineFunction({
  callback_id: "reverse",
  title: "Reverse",
  description: "Takes a string and reverses it, then sends to API",
  source_file: "functions/reverse.ts",
  input_parameters: {
    properties: {
      stringToReverse: {
        type: Schema.types.string,
        description: "The string to reverse",
      },
    },
    required: ["stringToReverse"],
  },
  output_parameters: {
    properties: {
      reversedString: {
        type: Schema.types.string,
        description: "The string in reverse",
      },
      apiResponseStatus: {
        type: Schema.types.number,
        description: "Status code from the API",
      },
      apiResponseMessage: {
        type: Schema.types.string,
        description: "Response message from the API",
      },
    },
    required: ["reversedString", "apiResponseStatus", "apiResponseMessage"],
  },
});

export default SlackFunction(
  ReverseFunctionDefinition,
  async ({ inputs }) => {
    const reversedString = inputs.stringToReverse;
    
    console.log("Reversed string:", reversedString);

    // Make a POST request to the API with the reversed string as the input key
    try {
      const response = await fetch("http://127.0.0.1:5000/send-url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input: reversedString }),
      });

      const responseMessage = await response.text();
      console.log("API Response Status:", response.status);
      console.log("API Response Message:", responseMessage);

      return {
        outputs: {
          reversedString,
          apiResponseStatus: response.status,
          apiResponseMessage: responseMessage,
        },
      };
    } catch (error) {
      console.error("Error sending to API:", error);
      return {
        outputs: {
          reversedString,
          apiResponseStatus: 500,
          apiResponseMessage: "Failed to send URL",
        },
      };
    }
  }
);
