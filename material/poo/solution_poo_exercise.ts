class VideoGame {
  constructor(
    readonly name: string,
    readonly releaseYear: number,
    readonly platforms: readonly VideoGameConsole[]
  ) {}

  toString() {
    return JSON.stringify(this, null, 4);
  }
}

class VideoGameConsole {
  constructor(
    readonly name: string,
    readonly releaseYear: number,
    readonly companyName: string
  ) {}

  toString() {
    return JSON.stringify(this, null, 4);
  }
}

class VideoGameServiceLocator {
  readonly degaDrive = new VideoGameConsole("DegaDrive", 1920, "Dega");
  readonly satourne = new VideoGameConsole("Satourne", 1950, "Dega");
  readonly nontendo = new VideoGameConsole("Nontendo", 1900, "Nontendo");
  readonly superNontendo = new VideoGameConsole(
    "Super Nontendo",
    1930,
    "Nontendo"
  );

  private constructor() {}

  private static readonly _instance = new VideoGameServiceLocator();

  static get instance(): VideoGameServiceLocator {
    return this._instance;
  }
}

function createDegaDriveVideoGame(
  name: string,
  releaseYear: number
): VideoGame {
  return new VideoGame(name, releaseYear, [
    VideoGameServiceLocator.instance.degaDrive,
  ]);
}

function createSuperNontendoVideoGame(
  name: string,
  releaseYear: number
): VideoGame {
  return new VideoGame(name, releaseYear, [
    VideoGameServiceLocator.instance.superNontendo,
  ]);
}

function createCrossPlatformVideoGame(
  name: string,
  releaseYear: number
): VideoGame {
  return new VideoGame(name, releaseYear, [
    VideoGameServiceLocator.instance.degaDrive,
    VideoGameServiceLocator.instance.satourne,
    VideoGameServiceLocator.instance.superNontendo,
    VideoGameServiceLocator.instance.nontendo,
  ]);
}

const retroGames = [
  createDegaDriveVideoGame("Super hydlike", 1931),
  createSuperNontendoVideoGame("Final Fiction", 1940),
  createCrossPlatformVideoGame("International Football", 1920),
];

console.table(retroGames);

console.log(retroGames.toString());
