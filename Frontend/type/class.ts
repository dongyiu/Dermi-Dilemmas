export enum SkinCondition {
    ActinicKeratosis,
    AtopicDermatitis,
    BenignKeratosis,
    Dermatofibroma,
    MelanocyticNevus,
    Melanoma,
    SquamousCellCarcinoma,
    TineaRingwormCandidiasis,
    VascularLesion
}

export function getSkinConditionByIndex(index: number): SkinCondition | undefined {
    const enumValues = Object.values(SkinCondition).filter(value => typeof value === 'number') as unknown as SkinCondition[];
    if (index >= 0 && index < enumValues.length) {
        return enumValues[index];
    }
    return undefined; // or you could throw an error, depending on how you want to handle an invalid index
}