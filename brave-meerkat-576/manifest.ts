import { Manifest } from "deno-slack-sdk/mod.ts";
import ReverseWorkflow from "./workflows/reverse_string.ts";

/**
 * The app manifest contains the app's configuration. This
 * file defines attributes like app name and description.
 * https://api.slack.com/automation/manifest
 */
export default Manifest({
  name: "brave-meerkat-576",
  description: "Post the reversed version of a string to a selected channel",
  icon: "assets/default_new_app_icon.png",
  workflows: [ReverseWorkflow],
  outgoingDomains: ["127.0.0.1"],
  botScopes: ["commands", "chat:write", "chat:write.public"],
});
