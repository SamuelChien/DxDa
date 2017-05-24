// Type definitions for OfficeBrowserFeedback
// Project: OfficeBrowserFeedback
// Definitions by: ocefeedback@microsoft.com

declare namespace OfficeBrowserFeedback {
	// The init options.
	let initOptions: IInitOptions;

	// The environment enum.
	enum Environment {
		Production,
		Int
	}

	// Interface for DismissDelegate.
	interface IOnDismissDelegate {
		(submitted: Boolean): void;
	}

	// Interface for UserVoiseInitOptions.
	interface IUserVoiceInitOptions {
		// Url for user voice.
		url: string;

		// Url for the user voice terms of service.
		termsOfServiceUrl: string;

		// Url for the user voice privacy policy.
		privacyPolicyUrl: string;
	}

	// Interface for initOptions.
	interface IInitOptions {
		appId: number;
		stylesUrl: string;
		intlUrl: string;
		environment?: Environment;
		sessionId?: string;
		build?: string;
		primaryColour?: string;
		secondaryColour?: string;
		onDismiss?: IOnDismissDelegate;
		locale?: string;
		bugForm?: boolean;
		userEmail?: string;
		screenshot?: boolean;
		userVoice?: IUserVoiceInitOptions;
	}

	// Create a single feedback dialog, where the feedback type is predetermined.
	// This actually returns a promise, typecast explicitly to use as promise.
	function singleFeedback(feedbackType: string): void;

	// Create a multi feedback dialog, where the feedback type is selected by the user.
	// This actually returns a promise, typecast explicitly to use as promise.
	function multiFeedback(): void;
}