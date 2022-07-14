// This file can be replaced during build by using the `fileReplacements` array.
// `ng build` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,

  OPENAI_API_KEY: "",

  temperature: 0.0,
  max_tokens: 250,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
  pretext: 'A program does the following: ',
  posttext: 'Generated [PROGLANG] Code: ',

  nl_temperature: 0.0,
  nl_max_tokens: 100,
  nl_top_p: 1,
  nl_frequency_penalty: 0,
  nl_presence_penalty: 0,
  nl_pretext: '',
  nl_posttext: 'Short Explanation of the code above:',
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.
