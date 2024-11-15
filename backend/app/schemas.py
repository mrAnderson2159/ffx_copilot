from pydantic import BaseModel
from typing import Optional


class ZoneBase(BaseModel):
    """Rappresenta la struttura base per una zona, con nome e URL opzionale dell'immagine."""
    name: str
    image_url: Optional[str] = None


class Zone(ZoneBase):
    """Rappresenta una zona nel database, con un ID per identificazione."""
    id: int

    class Config:
        from_attributes = True


class FiendBase(BaseModel):
    """Rappresenta la struttura base per un mostro, con nome, stato di cattura e URL opzionale dell'immagine."""
    name: str
    was_captured: Optional[int] = 0
    image_url: Optional[str] = None


class Fiend(FiendBase):
    """Rappresenta un mostro nel database, con un ID e il campo zone_id per la zona di appartenenza."""
    id: int
    zone_id: int

    class Config:
        from_attributes = True


class FiendCaptureUpdate(BaseModel):
    """Rappresenta l'aggiornamento del numero di catture di un mostro, con ID e variazione."""
    fiend_id: int
    delta: int


class FiendCapturesUpdateRequest(BaseModel):
    """Richiesta per aggiornare le catture dei mostri."""
    updates: list[FiendCaptureUpdate]


class FiendWithFound(BaseModel):
    native: list[Fiend]
    others: list[Fiend]


class ConquestResponseBase(BaseModel):
    """Base per la risposta delle conquiste, contenente il nome e lo stato di creazione."""
    name: str
    created: bool
    image_url: str
    reward: Optional[tuple[str, int]] = None


class AreaConquestBase(BaseModel):
    """Rappresenta la struttura base per una conquista di zona, con nome, immagine e stato di creazione."""
    name: str
    image_url: Optional[str] = None
    created: Optional[bool] = False
    defeated: Optional[bool] = False


class AreaConquestResponse(ConquestResponseBase):
    """Risposta per una conquista di zona."""

    class Config:
        from_attributes = True


class AreaConquest(AreaConquestBase):
    """Rappresenta una conquista di zona nel database, con un ID per identificazione."""
    id: int

    class Config:
        from_attributes = True


class SpeciesConquestBase(BaseModel):
    """Rappresenta la struttura base per una conquista di specie, con nome, immagine, requisiti e stato."""
    name: str
    image_url: Optional[str] = None
    required_fiends: int
    created: Optional[bool] = False
    defeated: Optional[bool] = False


class SpeciesConquestResponse(ConquestResponseBase):
    """Risposta per una conquista di specie."""

    class Config:
        from_attributes = True


class SpeciesConquest(SpeciesConquestBase):
    """Rappresenta una conquista di specie nel database, con un ID per identificazione."""
    id: int

    class Config:
        from_attributes = True


class OriginalCreationBase(BaseModel):
    """Rappresenta la struttura base per una creazione originale, con nome, immagine, regola e stato."""
    name: str
    image_url: Optional[str] = None
    created: Optional[bool] = False
    defeated: Optional[bool] = False
    creation_rule: Optional[str] = None


class OriginalCreationResponse(ConquestResponseBase):
    """Risposta per una creazione originale."""

    class Config:
        from_attributes = True


class OriginalCreation(OriginalCreationBase):
    """Rappresenta una creazione originale nel database, con un ID per identificazione."""
    id: int

    class Config:
        from_attributes = True


class ConquestRepr(BaseModel):
    id: int
    name: str
    image_url: str
    destination: str


class FullDetailsResponse(BaseModel):
    id: int
    name: str
    image_url: str
    created: Optional[bool] = False
    defeated: Optional[bool] = False
    creation_reward: Optional[tuple[str, int]] = None
    zone_id: Optional[int] = None
    zone_name: Optional[str] = None
    required_fiends: Optional[list[tuple[int, str]]] = None
    required_fiends_amount: Optional[int] = None
    creation_rule: Optional[str] = None
    hp: Optional[int] = None
    mp: Optional[int] = None
    overkill: Optional[int] = None
    ap: Optional[int] = None
    ap_overkill: Optional[int] = None
    guil: Optional[int] = None
    battle_reward: Optional[tuple[str, int]] = None
    weakness: Optional[list[tuple[str, int]]] = None
    resistance: Optional[list[str]] = None
    common_steal: Optional[tuple[str, int]] = None
    rare_steal: Optional[tuple[str, int]] = None

